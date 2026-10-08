"""Service module 44063: business logic, no crypto."""


def calculate_total_44063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44063():
    return 'module 44063 handles orders and invoices'
