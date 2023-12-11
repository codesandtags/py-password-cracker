# py password cracker

Verifies all possible combinations to get the password for a ZIP file with a simple password.

## State of the art

### Brute force

The brute force attack is a method that tries all possible combinations of characters until it finds the password. This method is very effective if the password is a combination of common words and numbers. The brute force attack is a very slow method, but it is very effective if the password is a combination of common words and numbers.

### Example of use

```bash
python3 brute-force.py -f tests/numbers-5.zip -l 5 -s 0123456789
```

### Dictionary attack

The common dictionary attack is a method that uses a list of words to try to find the password. This method is very effective if the password is a common word or a combination of common words. The dictionary attack is a very fast method, but it is not very effective if the password is not a common word.

[Rock You common password list](https://www.kaggle.com/datasets/wjburns/common-password-list-rockyoutxt) is a list of 14,344,391 real passwords used by real people.

### Example of use

```bash
python3 dictionary.py -f tests/numbers-5.zip -d dictionary/dictionary.txt
```

## Using hashcat and john the ripper

Hashcat is the **world's fastest and most advanced password recovery utility**, supporting five unique modes of attack for over 200 highly-optimized hashing algorithms. Hashcat currently supports CPUs, GPUs, and other hardware accelerators on Linux, Windows, and macOS, and has facilities to help enable distributed password cracking.

- [Hashcat](https://hashcat.net/hashcat/)
- [Hashcat homebrew](https://formulae.brew.sh/formula/hashcat)
- [John the ripper](https://www.openwall.com/john/)
- [John the ripper homebrew](https://formulae.brew.sh/formula/john-jumbo)

hashcat options:

- `-m --hash-type`: Hash type
- `-a`: Attack mode. 0 = Straight, 1 = Combination, 3 = Brute-force, 6 = Hybrid dict + mask, 7 = Hybrid mask + dict
- `-w`: Workload profile. 1 = Low, 2 = Medium, 3 = High
- `-O`: Optimize kernel
- `-o`: Output file
- `--show`: Prints the cracked password to the screen and the hash to the right of the password
- `--identify`: Identifies the hash type of a hash or file

hashcat patterns:

- `?d`: Numbers
- `?l`: Lowercase letters
- `?u`: Uppercase letters
- `?s`: Symbols
- `?a`: All characters
- `?b`: Custom characters
- `?1`: Custom mask

### Example of use

#### 1. Identify hash type

To identify the hash type of a hash or file, the best way is using zip2john.

```bash
zip2john tests/numbers-5.zip > tests/numbers-5-hash.txt
```

After that edit, the file and copy the hash.

```bash
cat tests/numbers-5-hash.txt
```

And finally, use hashcat to identify the hash type.

```bash
hashcat --identify tests/numbers-5-hash.txt
```

This will generate something like this:

```bash
hashcat --identify tests/numbers-5-hash.txt
The following 2 hash-modes match the structure of your input hash:

      # | Name                                                       | Category
  ======+============================================================+======================================
  17225 | PKZIP (Mixed Multi-File)                                   | Archive
  17210 | PKZIP (Uncompressed)                                       | Archive
```

### 2. Dictionary attack

Once you have identified the hash type, you can use hashcat to crack the password.

```bash
hashcat --show -m [hash-type] -a [attack-mode] [hash-file] [dictionary-file]
```

```bash
hashcat --show -m 17225 -a 3 tests/numbers-5.txt dictionary/dictionary.txt
```

### Hybrid attack

The hybrid attack is a method that combines the brute force and dictionary attack methods. This method is very effective if the password is a combination of common words and numbers. The hybrid attack is a very fast method, but it is not very effective if the password is not a combination of common words and numbers.

## Tests table

**Time in seconds.**

| File name      | Password         | T. Bruteforce  | T. Dictionary   | T. Hashcat |
| -------------- | ---------------- | -------------- | --------------- | ---------- |
| numbers-5.zip  | 12345            | 1.035          | 0.5972          | 0.038      |
| numbers-8.zip  | 12345678         | 1063.3985      | 0.6026          | 0.039      |
| numbers-12.zip | 123456789012     | 1.035          | 5.8381          | 0.038      |
| numbers-16.zip | 1611122233344499 | months? (FAIL) | 670.9195 (FAIL) | 0.041      |

## State of art

- https://www.csoonline.com/article/569355/hashcat-explained-why-you-might-need-this-password-cracker.html
