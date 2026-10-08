"""Service module 39168: business logic, no crypto."""


def calculate_total_39168(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39168():
    return 'module 39168 handles orders and invoices'
