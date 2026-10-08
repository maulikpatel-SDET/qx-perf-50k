"""Service module 37209: business logic, no crypto."""


def calculate_total_37209(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37209():
    return 'module 37209 handles orders and invoices'
