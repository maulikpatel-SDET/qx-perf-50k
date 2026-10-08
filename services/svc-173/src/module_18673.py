"""Service module 18673: business logic, no crypto."""


def calculate_total_18673(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18673():
    return 'module 18673 handles orders and invoices'
