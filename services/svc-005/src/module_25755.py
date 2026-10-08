"""Service module 25755: business logic, no crypto."""


def calculate_total_25755(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25755():
    return 'module 25755 handles orders and invoices'
