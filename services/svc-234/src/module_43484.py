"""Service module 43484: business logic, no crypto."""


def calculate_total_43484(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43484():
    return 'module 43484 handles orders and invoices'
