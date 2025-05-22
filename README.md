# Hebrew Vocabulary Trainer 🇮🇱

A comprehensive command-line vocabulary training application for learning Hebrew words with English translations. The application includes editing, training, and testing modes with AWS S3 integration for data persistence.

## Features ✨

### 🔧 Editing Mode
- **Add words**: Add new vocabulary words to specific units
- **Delete words**: Remove words from vocabulary units
- **Update words**: Modify existing words and their meanings
- **List words**: Display all words in a specific unit
- **Search words**: Find words across all units

### 🎓 Training Mode
- **Train whole unit**: Practice all words in a unit with customizable timing and repetitions
- **Train word range**: Practice a specific range of words within a unit
- **Randomized order**: Words are shuffled for better learning
- **Customizable timing**: Set delay time and repetition count

### 📝 Testing Mode
- **Unit testing**: Take quizzes on specific vocabulary units
- **Score tracking**: Get detailed feedback on performance
- **Review incorrect answers**: See which words need more practice
- **Performance feedback**: Motivational messages based on score

### ☁️ Cloud Integration
- **AWS S3 backup**: Automatic synchronization with S3 bucket
- **Version control**: S3 versioning support for data safety
- **Cross-device access**: Access your vocabulary from anywhere

## Installation 📦

### Prerequisites
- Python 3.7+
- AWS account (for S3 integration)
- boto3 library

### Setup Instructions

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd hebrew-vocab-trainer
   ```

2. **Install required dependencies**
   ```bash
   pip install boto3
   ```

3. **Configure AWS credentials**
   - Set up AWS CLI or configure environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=us-west-2
   ```

4. **Initialize S3 bucket** (optional)
   - The application will create the bucket automatically
   - Default bucket name: `vocab-trainer`
   - Default region: `us-west-2`

## File Structure 📁

```
hebrew-vocab-trainer/
├── main.py                 # Main application entry point
├── menus.py               # User interface menus
├── editing_mode.py        # Word editing functionality
├── training_func.py       # Training mode functions
├── testing_func.py        # Testing mode functions
├── handle_vocab_file.py   # File handling operations
├── s3.py                  # AWS S3 integration
├── validation.py          # Input validation utilities
├── vocab_hebrew.json      # Vocabulary data file
└── README.md             # This file
```

## Usage 🚀

### Starting the Application
```bash
python main.py
```

### Main Menu Options
1. **Editing Mode** - Manage your vocabulary
2. **Training Mode** - Practice vocabulary
3. **Testing Mode** - Quiz yourself
4. **Exit** - Close the application

### Sample Vocabulary Units
The application comes with sample Hebrew vocabulary:
- **Unit 1**: Fruits (apple, banana, grape, orange, pear)
- **Unit 2**: School items (book, pen, pencil, school, teacher)
- **Unit 3**: Nature (sun, moon, star, cloud, rain)

## Configuration ⚙️

### S3 Settings
Edit `s3.py` to customize:
- Bucket name
- AWS region
- File name

### Default Training Settings
- **Timeout**: 4 seconds per word
- **Repetitions**: 7 rounds
- **Randomization**: Enabled by default

## Download Links 📥

### Option 1: Individual Files
Download each file individually:

- [`main.py`](./main.py) - Main application
- [`menus.py`](./menus.py) - Menu system
- [`editing_mode.py`](./editing_mode.py) - Editing functions
- [`training_func.py`](./training_func.py) - Training functions
- [`testing_func.py`](./testing_func.py) - Testing functions
- [`handle_vocab_file.py`](./handle_vocab_file.py) - File operations
- [`s3.py`](./s3.py) - AWS S3 integration
- [`validation.py`](./validation.py) - Input validation
- [`vocab_hebrew.json`](./vocab_hebrew.json) - Sample vocabulary

### Option 2: Complete Package
```bash
# Create a new directory
mkdir hebrew-vocab-trainer
cd hebrew-vocab-trainer

# Download all files (replace with your actual file URLs)
curl -O <base-url>/main.py
curl -O <base-url>/menus.py
curl -O <base-url>/editing_mode.py
curl -O <base-url>/training_func.py
curl -O <base-url>/testing_func.py
curl -O <base-url>/handle_vocab_file.py
curl -O <base-url>/s3.py
curl -O <base-url>/validation.py
curl -O <base-url>/vocab_hebrew.json
```

### Option 3: GitHub Repository
If hosted on GitHub:
```bash
git clone https://github.com/yourusername/hebrew-vocab-trainer.git
```

## API Reference 📚

### Key Functions

#### Editing Functions
- `add_word(vocab, unit, word, meaning)` - Add new vocabulary word
- `delete_word(vocab, unit, word)` - Remove word from unit
- `update_word(vocab, unit, old_word, new_word, new_meaning)` - Update existing word
- `list_words(vocab, unit)` - Display all words in unit
- `search_word(vocab, word)` - Find word across all units

#### Training Functions
- `train_whole_unit(timeout, repeat_count, unit)` - Train entire unit
- `train_words_range(vocab, repeat_count, timeout, unit, start_index, end_index)` - Train word subset
- `show_random(vocab, unit)` - Randomize word order

#### Testing Functions
- `test(vocab, unit)` - Run vocabulary quiz
- `get_feedback(score)` - Provide performance feedback

## Troubleshooting 🔧

### Common Issues

1. **AWS Credentials Error**
   - Ensure AWS credentials are properly configured
   - Check IAM permissions for S3 access

2. **File Not Found Error**
   - Ensure `vocab_hebrew.json` exists in the same directory
   - Check file permissions

3. **Import Errors**
   - Verify all Python files are in the same directory
   - Install required dependencies: `pip install boto3`

4. **S3 Upload Failures**
   - Check internet connection
   - Verify bucket permissions
   - Ensure region is correctly set

## Contributing 🤝

Feel free to contribute to this project by:
- Adding new vocabulary units
- Improving the user interface
- Adding new training modes
- Enhancing S3 integration
- Adding support for other languages

## License 📄

This project is open source and available under the [MIT License](LICENSE).

## Support 💬

For questions or support:
- Create an issue in the repository
- Contact the developer
- Check the troubleshooting section above

---

**Happy Learning! 🎉**

*Master Hebrew vocabulary one word at a time!*
