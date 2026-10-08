"""Service module 22326: business logic, no crypto."""


def calculate_total_22326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22326():
    return 'module 22326 handles orders and invoices'
