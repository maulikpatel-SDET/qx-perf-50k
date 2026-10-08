"""Service module 43066: business logic, no crypto."""


def calculate_total_43066(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43066():
    return 'module 43066 handles orders and invoices'
