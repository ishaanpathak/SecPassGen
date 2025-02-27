# SecPassGen

A simple python tool to generate pretty secure passphrases

# How does it work

The script generates words using the [Diceware method](#diceware-method), for which it requires random numbers. The script primarily uses random numbers from [random.org/integer](https://www.random.org/integers/) but an argument is provided to run it offline as well. The only reason random.org has been used is because the service provides actual random numbers as compared to pseudo random numbers that the random library provides.

Once the script has the words it needs, it generates the passwords based on the rules provided. The default rule is to capitalize each word's first letter and add a random number anywhere in the passphrase. The rules can be changed using the arguments but the default rules provide best security as compared to other configuration(s).

# How to Use

You must first clone the repository anywhere you want and then navigate to the folder where it is cloned.

```bash
git clone https://github.com/ishaanpathak/SecPassGen.git
cd SecPassGen
```

# Running with [uv](https://docs.astral.sh/uv/)

If you are using or want to use [uv](https://docs.astral.sh/uv/), make sure it is installed and is added to path. And then run the following command below.

```bash
uv run ./main.py [arguments]
```

# Running normally

First, install the requirements using the command below.

```bash
pip install -r requirements.txt
```

Then, use the program using the following command:

```bash
python ./main.py [arguments]
```

The arguments are completely **optional** but in case you want to modify how the passwords are generated or want to generate more than one password, you can use either of the following commands to get help

```bash
python ./main.py -h
python ./main.py --help
```

# Arguments / Flags

All arguments are entirely **optional**. However, if you'd like to customize the password generation process or generate multiple passwords, you can use these arguments.

| Flag   | Flag (Long)         | Function                             |
| ------ | ------------------- | ------------------------------------ |
| -h     | --help              | show this help message and exit      |
| -nc    | --no-cap            | Exclude Capital Letters              |
| -nn    | --no-num            | Exclude Numbers                      |
| -jp    | --japanese          | Use Japanese Wordlist                |
| -w W   | --words W           | Number of words to use               |
| -s S   | --separator S       | Separator symbol to use              |
| -o     | --offline           | Use Python's Random Number Generator |
| -pc PC | --password-count PC | Number of Passwords to Generate      |

# Diceware Method

The Diceware Method is a method of getting words using a Dice. We already have a wordlist provided to use that has all the words paired with their 5 digit numbers. We roll the dice 5 times and get a number. We use that number to get a number from the wordlist and repeat this process for however many words we require. For example, if we want a 5 word passphrase, we will throw the dice 25 times to give 5 pairs of 5 digit number.

You can get more information on the Diceware Method at https://theworld.com/~reinhold/diceware.html
