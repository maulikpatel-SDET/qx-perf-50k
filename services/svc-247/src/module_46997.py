"""Service module 46997: business logic, no crypto."""


def calculate_total_46997(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46997():
    return 'module 46997 handles orders and invoices'
