# Ticket System

## Description

A ticket system that allows users to submit and manage help desk tickets on python base. It provides features to create, update, and display tickets, as well as statistics on ticket status.

## Prerequisites

Ensure you have Python installed on your system. Download the latest version from [python.org](https://www.python.org/).

## Features

- Users can submit help desk tickets by providing relevant information.
- Tickets are assigned a unique ticket number and are tracked by their status.
- The system allows responding to tickets, changing their status, and reopening closed tickets.
- Provides a statistical overview of ticket creation, resolution, and open/reopened tickets.

## How to Use

1. Run the `ticket_system.py` script.
2. Follow the on-screen menu to perform actions like submitting a ticket, displaying all tickets, responding to a ticket, reopening a resolved ticket, or viewing ticket statistics.

## Design Principles and Integration

The Ticket System adheres to design principles and integrates the Observer design pattern. The Observer pattern is applied to separate the subject (ticket logic) and observer (display logic). The Single Responsibility Principle (SRP) is followed, ensuring each class has a single responsibility. Additionally, the Open/Closed Principle (OCP) is considered, allowing for easy extension without modifying the core ticket logic. This enhances maintainability and extensibility by promoting a modular and loosely-coupled architecture.

## License

This project is licensed under the [MIT License](LICENSE).
