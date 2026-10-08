"""Service module 24792: business logic, no crypto."""


def calculate_total_24792(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24792():
    return 'module 24792 handles orders and invoices'
