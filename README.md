# Research Repository

This Research Repository explores the implementation of design patterns, SOLID principles, and practice codes for Python learning journey.

## Practice

The `practice` folder contains various Python code for practicing with examples from the course material.

## Design Patterns

The `design patterns` folder includes implementations of various design patterns in Python. The following design patterns are explored:

- **Decorator Pattern**: Refactoring for the Single-Responsibility Principle (SRP) aligns with the Decorator Pattern, where behavior (compression) is added to individual objects (FileManager, ZipFileManager) rather than the entire class.

- **Abstract Factory Pattern**: The Open-Closed Principle (OCP) is addressed through the use of an Abstract Factory Pattern with the introduction of the Shape abstract base class and its concrete subclasses.

- **Strategy Pattern**: The Liskov Substitution Principle (LSP) aligns with the Strategy Pattern by having different strategies (calculate_area method) implemented in interchangeable classes (Circle, Rectangle, Square).

- **Observer Pattern**: Implementation for Tic Tac Toe (tic-tac-toe folder) demonstrates the Observer Pattern, where the observable (game) notifies its observers (players) about the state changes.

- **Singleton Pattern**: Code for the Ticket System (ticket system folder) follows the Singleton Pattern, ensuring a single instance of the ticket system exists throughout the application.

## SOLID Principles

### Overview

This repository explores the implementation of SOLID principles in Python through practical code examples. The SOLID principles are a set of five object-oriented design principles aimed at promoting clean, maintainable, and scalable code. Each principle is demonstrated through refactoring Python code snippets.

### Exploration of Design Patterns:

- **Single-Responsibility Principle (SRP)**: Aligns with the Decorator Pattern.
- **Open-Closed Principle (OCP)**: Addressed through the use of an Abstract Factory Pattern.

- **Liskov Substitution Principle (LSP)**: Aligns with the Strategy Pattern.

- **Interface Segregation Principle (ISP)**: Refactor follows the Interface Segregation Principle itself.

- **Dependency Inversion Principle (DIP)**: Demonstrated through Dependency Injection.

### Analysis of Design Principles:

- **SRP**: Ensures that each class has a single reason to change, promoting maintainability and reducing the risk of bugs when modifications are needed.

- **OCP**: Allows for extension without modification, enabling scalability and flexibility when adding new shapes without altering existing code.

- **LSP**: Ensures that subclasses can be used interchangeably with their base classes, promoting polymorphism and avoiding unexpected behavior.

- **ISP**: Ensures that classes only depend on the methods they use, preventing unnecessary coupling and promoting a more modular design.

- **DIP**: Allows for flexibility in choosing dependencies, promoting abstraction and reducing direct dependencies on concrete implementations.

## Github Repository 

[Github Repository](https://github.com/Minjijung0331/IT5016D)

## License

This code is provided under the [MIT License](LICENSE).
