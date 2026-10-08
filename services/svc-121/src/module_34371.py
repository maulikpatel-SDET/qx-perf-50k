"""Service module 34371: business logic, no crypto."""


def calculate_total_34371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34371():
    return 'module 34371 handles orders and invoices'
