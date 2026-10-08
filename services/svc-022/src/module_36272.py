"""Service module 36272: business logic, no crypto."""


def calculate_total_36272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36272():
    return 'module 36272 handles orders and invoices'
