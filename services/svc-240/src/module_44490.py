"""Service module 44490: business logic, no crypto."""


def calculate_total_44490(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44490():
    return 'module 44490 handles orders and invoices'
