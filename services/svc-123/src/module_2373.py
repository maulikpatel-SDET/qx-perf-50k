"""Service module 2373: business logic, no crypto."""


def calculate_total_2373(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2373():
    return 'module 2373 handles orders and invoices'
