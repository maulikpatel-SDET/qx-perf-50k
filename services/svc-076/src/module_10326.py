"""Service module 10326: business logic, no crypto."""


def calculate_total_10326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10326():
    return 'module 10326 handles orders and invoices'
