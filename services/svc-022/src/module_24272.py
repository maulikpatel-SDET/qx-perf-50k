"""Service module 24272: business logic, no crypto."""


def calculate_total_24272(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24272():
    return 'module 24272 handles orders and invoices'
