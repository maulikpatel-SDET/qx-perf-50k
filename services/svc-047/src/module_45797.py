"""Service module 45797: business logic, no crypto."""


def calculate_total_45797(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45797():
    return 'module 45797 handles orders and invoices'
