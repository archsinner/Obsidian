## Interactive mode[](https://elixir-lang.org/getting-started/introduction.html#interactive-mode "Link here")[](https://elixir-lang.org/getting-started/introduction.html#toc "Back to Table of Contents")
[[Elixir Introduction]]
When you install Elixir, you will have three new executables: `iex`, `elixir` and `elixirc`. If you compiled Elixir from source or are using a packaged version, you can find these inside the `bin` directory.

For now, let’s start by running `iex` (or `iex.bat` if you are on Windows PowerShell, where `iex` is a PowerShell command) which stands for Interactive Elixir. In interactive mode, we can type any Elixir expression and get its result. Let’s warm up with some basic expressions.

Open up `iex` and type the following expressions:

```
Erlang/OTP 22.0 [64-bit] [smp:2:2] [...]

Interactive Elixir (1.13.4) - press Ctrl+C to exit
iex(1)> 40 + 2
42
iex(2)> "hello" <> " world"
"hello world"
```

Please note that some details like version numbers may differ a bit in your session; that’s not important. From now on `iex` sessions will be stripped down to focus on the code. To exit `iex` press `Ctrl+C` twice.

It seems we are ready to go! We will use the interactive shell quite a lot in the next chapters to get a bit more familiar with the language constructs and basic types, starting in the next chapter.

> Note: if you are on Windows, you can also try `iex --werl` (`iex.bat --werl` on PowerShell) which may provide a better experience depending on which console you are using.