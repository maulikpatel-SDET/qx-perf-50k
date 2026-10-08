"""Service module 37856: business logic, no crypto."""


def calculate_total_37856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37856():
    return 'module 37856 handles orders and invoices'
