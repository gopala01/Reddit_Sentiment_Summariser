from transformers import PegasusForConditionalGeneration, PegasusTokenizer, Trainer, TrainingArguments
import pandas as pd
from datasets import Dataset


model_name = 'google/pegasus-xsum'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name)

train_dataset = pd.read_csv("train_dataset.csv")
val_dataset = pd.read_csv("val_dataset.csv")

print(train_dataset.columns)

def preprocess_data(examples):
    model_inputs = tokenizer(examples['article'], max_length=512, truncation=True, padding="max_length")
    # Tokenize the summaries and add the `labels` field
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples['highlights'], max_length=128, truncation=True, padding="max_length")
    model_inputs['labels'] = labels['input_ids']
    return model_inputs

# Convert the Pandas DataFrames to Hugging Face Dataset objects
train_dataset = Dataset.from_pandas(train_dataset)
val_dataset = Dataset.from_pandas(val_dataset)

# Apply the preprocessing function
train_dataset = train_dataset.map(preprocess_data, batched=True)
val_dataset = val_dataset.map(preprocess_data, batched=True)

# Set the format for PyTorch
train_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])
val_dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])




training_args = TrainingArguments(
    output_dir='./results',          # Output directory for model checkpoints
    num_train_epochs=1,              # Number of training epochs
    per_device_train_batch_size=4,   # Batch size for training
    per_device_eval_batch_size=4,    # Batch size for evaluation
    warmup_steps=500,                # Number of warmup steps
    weight_decay=0.01,               # Strength of weight decay
    logging_dir='./logs',            # Directory for storing logs
    evaluation_strategy="steps",     # Evaluate every `logging_steps`
    logging_steps=100,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,    # Training dataset
    eval_dataset=val_dataset        # Your validation dataset
)

trainer.train()


