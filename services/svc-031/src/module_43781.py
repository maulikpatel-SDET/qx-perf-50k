"""Service module 43781: business logic, no crypto."""


def calculate_total_43781(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43781():
    return 'module 43781 handles orders and invoices'
