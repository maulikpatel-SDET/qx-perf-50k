"""Service module 21193: business logic, no crypto."""


def calculate_total_21193(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21193():
    return 'module 21193 handles orders and invoices'
