"""Service module 5469: business logic, no crypto."""


def calculate_total_5469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5469():
    return 'module 5469 handles orders and invoices'
