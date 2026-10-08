"""Service module 23755: business logic, no crypto."""


def calculate_total_23755(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23755():
    return 'module 23755 handles orders and invoices'
