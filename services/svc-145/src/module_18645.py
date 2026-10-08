"""Service module 18645: business logic, no crypto."""


def calculate_total_18645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18645():
    return 'module 18645 handles orders and invoices'
