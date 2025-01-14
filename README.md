# Circus computations
🧮 The most overcomplicated homework for Numerical analysis

## Preamble
![image](https://github.com/BeaverNotACat/Circus-computations/blob/main/assets/example.PNG?raw=true)
I needed to write a desmos-like graphing calculator and calculate an equalation with it.
One of the requerements was create project structure with some procedural stuff. But i thout it would be too easy and implemented some type of clean architecture.

## How to run
``

## Project structure
```
src
└── circus
    ├── adapters         # adapters that provide rendering, 
    │   └── . . .        #     computatuional abstractions and cli functions
    ├── applications     # Clean arhitecture applicatiobn layer
    │   ├── figures      # Mathematical computations 
    │   │   └── . . .    #     + renderind usecases
    │   ├── gateway.py   # All adapter abstractions
    │   └── show.py      # Show graph usecase
    ├── app.py           # Application entrypoint
    ├── domain           # Domain layer
    │   └── models.py    # Domain models
    ├── ioc.py           # Factory of usecases with populated adapters
    ├── presentation     # Presentation layer
    │   └── . . .        #     with requested formulas
    └── settings.py      # Calculator settings
```

## Project stack
- Python 3.12
- Rye
- dependency-injector
- pillow
- pydantic-settings
