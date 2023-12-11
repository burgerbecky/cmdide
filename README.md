# cmdide - A tool to launch CodeWarrior from a command line

cmdide allows the compilation of Metrowerks CodeWarrior projects from the command line in MacOSX. CodeWarrior is a legacy development system for Mac OS and Mac OSX applications for the 680x0 and PowerPC. It's a desktop application that responds to AppleEvents.

This tool sends those events from a command line so CodeWarrior projects can be manipulated from a MacOSX command line.

cmdide is licensed under the MIT license, for details see LICENSE.txt.

## Usage

```text
cmdide
    --help             print this message
    --version          print the version of cmdide

    -diff [-ibs] [-y idepath] source destination
      -i               ignore case
      -b               ignore extra whitespace
      -s               display files that are the same
                       when comparing directories
      -t timeout       specify a number of seconds to wait for an ide reply
      -y idepath       use a specific ide by its pathname

    -proj [-bceqrwx] [-t timeout] [-y idepath] [-z targetname] projectfile
      -x               convert project when opening
      -r               remove objects from project
      -t timeout       specify a number of seconds to wait for an ide reply
      -y idepath       use a specific ide by its pathname
      -z targetname    switch to named target
      -w               print build warnings
      -e               print build errors
      -f filename      send errors and warnings output to a file
      -b               build target
      -c               close target after building
      -q               quit IDE after building
```

### Compatibility

cmdide runs on both 32 and 64 bit PowerPC and Intel Mac computers running MacOSX Leopard (10.5.8) or earlier.

The code is only built in 32 bit mode due to Carbon doesn't not exist in 64 bit, and that since CodeWarrior is only a 32 bit app, it's a moot point

### Bugs

Email the bug to [becky@burgerbecky.com](mailto:becky@burgerbecky.com) and mention python version, integer size (32 bit or 64 bit) and what version of Mac OSX

### Why?!?!?

There are those who'd ask, why in the world did I write this in the first place?

Metrowerks had this tool written only for PowerPC and it ran fine on my PowerPC Mac, however when Apple Introduced the Intel Macintosh, I asked Metrowerks for an Intel version of this tool. Metrowerks was already phasing out CodeWarrior and chose not to update this tool, which I relied on for automated builds of legacy apps (PowerPC and 680x0). I rolled up my sleeves and created an app that duplicated the original's operation and compiled it for both PowerPC and Intel Mac. It allowed my build system to continue to allow my code to be tested with the Metrowerks compiler for compatibilty (Their warnings find some very subtle issues in my code that help me keep my code quality high).

Sadly, Rosetta, the PowerPC emulation layer was retired after Snow Leopard so, while this tool runs on all Intel Macs, it's usefulness is limited to PowerPC Macs and Intel Macs that are still compatible with Rosetta.

Explore the dark regions of AppleEvents by looking at this code. Go mad. I did. It's not bad after you get used to the insanity.

Rebecca Ann Heineman

[burgerbecky.com](https://www.burgerbecky.com)

[Olde Skuul](https://www.oldeskuul.com)
