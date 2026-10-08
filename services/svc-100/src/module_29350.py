"""Service module 29350: business logic, no crypto."""


def calculate_total_29350(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29350():
    return 'module 29350 handles orders and invoices'
