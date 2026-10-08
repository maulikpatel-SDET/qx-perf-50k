"""Service module 43196: business logic, no crypto."""


def calculate_total_43196(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43196():
    return 'module 43196 handles orders and invoices'
