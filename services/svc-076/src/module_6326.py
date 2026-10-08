"""Service module 6326: business logic, no crypto."""


def calculate_total_6326(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6326():
    return 'module 6326 handles orders and invoices'
