"""Service module 43591: business logic, no crypto."""


def calculate_total_43591(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43591():
    return 'module 43591 handles orders and invoices'
