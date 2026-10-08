"""Service module 7781: business logic, no crypto."""


def calculate_total_7781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7781():
    return 'module 7781 handles orders and invoices'
