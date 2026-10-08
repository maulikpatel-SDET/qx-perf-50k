"""Service module 49645: business logic, no crypto."""


def calculate_total_49645(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49645():
    return 'module 49645 handles orders and invoices'
