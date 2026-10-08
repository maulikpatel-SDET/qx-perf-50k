"""Service module 2591: business logic, no crypto."""


def calculate_total_2591(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2591():
    return 'module 2591 handles orders and invoices'
