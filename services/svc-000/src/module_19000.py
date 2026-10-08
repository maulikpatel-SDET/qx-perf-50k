"""Service module 19000: business logic, no crypto."""


def calculate_total_19000(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19000():
    return 'module 19000 handles orders and invoices'
