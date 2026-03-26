# letterjoy-cipher-tool

A command-line tool for encoding and decoding ciphers from the [Letterjoy](https://letterjoy.com) subscription service.

## Installation

```bash
pip install -e .
```

## Usage

```
letterjoy --<cipher-type> (--encode | --decode) --cipherkey <file> [message]
```

The message can be supplied in three ways:
- As a quoted string: `--message "LRHCS NIIUP ..."`
- As a file argument: `letterjoy ... message.txt`
- Via stdin: `cat message.txt | letterjoy ...`

### Polyalphabetic substitution cipher

```bash
# Decode an encoded message from a file
letterjoy --polysubstitution --decode --cipherkey "Substitution Cipher Key.txt" "Substitution Cipher Encoded Message.txt"

# Encode a plaintext message
letterjoy --polysubstitution --encode --cipherkey key.txt --message "HELLO WORLD"

# Pipe a message
cat encoded.txt | letterjoy --polysubstitution --decode --cipherkey key.txt
```

## Cipher key format

Each line of the key file is a 26-character substitution alphabet, mapping A–Z to encoded characters. The number of lines equals the cipher period — for example, a 5-line key encodes every 5th letter with the same alphabet (letters 1, 6, 11, … use row 1; letters 2, 7, 12, … use row 2; and so on). Spaces in the message are ignored during encoding and decoding.

Example key (5-row, period 5):
```
GHIJKLMNOPQRSTUVWXYZABCDEF
EFGHIJKLMABCDNOPQRSTZUVWXY
AZYBXCWDVEFUTGHSRIJQKPLMON
QRSZUVWXYZBACEDFHGJILKMONP
DEGFIHJABCKOLMNPRQTSVUZXYW
```
