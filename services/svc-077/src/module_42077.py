"""Service module 42077: business logic, no crypto."""


def calculate_total_42077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42077():
    return 'module 42077 handles orders and invoices'
