"""Service module 39947: business logic, no crypto."""


def calculate_total_39947(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39947():
    return 'module 39947 handles orders and invoices'
