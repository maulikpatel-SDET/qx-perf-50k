"""Service module 46373: business logic, no crypto."""


def calculate_total_46373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46373():
    return 'module 46373 handles orders and invoices'
