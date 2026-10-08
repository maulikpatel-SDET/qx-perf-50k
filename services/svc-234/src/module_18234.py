"""Service module 18234: business logic, no crypto."""


def calculate_total_18234(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18234():
    return 'module 18234 handles orders and invoices'
