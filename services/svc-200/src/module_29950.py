"""Service module 29950: business logic, no crypto."""


def calculate_total_29950(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29950():
    return 'module 29950 handles orders and invoices'
