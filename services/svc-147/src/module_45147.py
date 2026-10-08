"""Service module 45147: business logic, no crypto."""


def calculate_total_45147(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45147():
    return 'module 45147 handles orders and invoices'
