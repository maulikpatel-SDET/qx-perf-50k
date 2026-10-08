"""Service module 16326: business logic, no crypto."""


def calculate_total_16326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16326():
    return 'module 16326 handles orders and invoices'
