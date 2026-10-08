"""Service module 35326: business logic, no crypto."""


def calculate_total_35326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35326():
    return 'module 35326 handles orders and invoices'
