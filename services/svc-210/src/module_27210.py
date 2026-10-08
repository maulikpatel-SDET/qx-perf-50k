"""Service module 27210: business logic, no crypto."""


def calculate_total_27210(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27210():
    return 'module 27210 handles orders and invoices'
