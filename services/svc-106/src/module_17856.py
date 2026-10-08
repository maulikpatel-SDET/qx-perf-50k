"""Service module 17856: business logic, no crypto."""


def calculate_total_17856(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17856():
    return 'module 17856 handles orders and invoices'
