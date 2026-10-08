"""Service module 49402: business logic, no crypto."""


def calculate_total_49402(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49402():
    return 'module 49402 handles orders and invoices'
