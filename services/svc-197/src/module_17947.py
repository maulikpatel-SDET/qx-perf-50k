"""Service module 17947: business logic, no crypto."""


def calculate_total_17947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17947():
    return 'module 17947 handles orders and invoices'
